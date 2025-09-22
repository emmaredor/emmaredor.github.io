"""
Vercel Serverless Function for Batch Student Transcript Generation
"""

import json
import yaml
import tempfile
import os
import sys
from http.server import BaseHTTPRequestHandler
import base64
import zipfile
from io import BytesIO
from datetime import datetime

# Add the lib directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from data_loader import DataLoader
from lightweight_excel import LightweightExcelLoader
from text_formatter import TextFormatter
from pdf_generator import TranscriptPDFGenerator
from grades_processor import GradeValidator


class BatchTranscriptGenerator:
    """Main class for batch transcript generation operations."""
    
    def __init__(self):
        self.data_loader = DataLoader()
        self.excel_loader = LightweightExcelLoader()
        self.text_formatter = TextFormatter()
        self.pdf_generator = TranscriptPDFGenerator()
        self.grade_validator = GradeValidator()


def handler(request):
    """
    Vercel serverless function handler for batch transcript generation.
    
    Expected POST request with multipart/form-data containing:
    - students_excel: Excel file content with students data
    - author_info: YAML file content
    """
    
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Parse the multipart form data
        content_type = request.headers.get('content-type', '')
        if 'multipart/form-data' not in content_type:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Expected multipart/form-data'})
            }
        
        # Get the request body
        body = request.get('body', '')
        if isinstance(body, str):
            body = body.encode('utf-8')
        
        # Parse form data
        form_data = parse_multipart_form_data(body, content_type)
        
        # Validate required files
        required_files = ['students_excel', 'author_info']
        for file_key in required_files:
            if file_key not in form_data:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({'error': f'Missing required file: {file_key}'})
                }
        
        # Initialize batch transcript generator
        generator = BatchTranscriptGenerator()
        
        # Parse author info
        try:
            author_data = yaml.safe_load(form_data['author_info'])
        except yaml.YAMLError as e:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Invalid author YAML format: {str(e)}'})
            }
        
        # Process Excel file
        try:
            # Get Excel content as bytes
            excel_content = form_data['students_excel']
            if isinstance(excel_content, str):
                excel_content = excel_content.encode('latin1')
            
            # Load students from Excel content directly
            students_data = generator.excel_loader.load_students_from_excel_content(excel_content)
        except Exception as e:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Error processing Excel file: {str(e)}'})
            }
            
            if not students_data:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({'error': 'No valid student data found in Excel file'})
                }
            
            # Load text templates
            text_templates_path = os.path.join(os.path.dirname(__file__), 'assets', 'text.json')
            with open(text_templates_path, 'r', encoding='utf-8') as f:
                text_templates = json.load(f)
            
            # Generate PDFs for all students
            generated_files = []
            pdf_directory = os.path.join(temp_dir, 'pdfs')
            os.makedirs(pdf_directory, exist_ok=True)
            
            for i, student_record in enumerate(students_data):
                try:
                    # Combine student and author data
                    combined_data = generator.text_formatter.combine_student_author_data(
                        student_record,
                        {'author': author_data.get('author', author_data)}
                    )
                    
                    # Validate required fields
                    if not generator.text_formatter.validate_required_fields(combined_data):
                        print(f"Skipping student {i+1}: Missing required fields")
                        continue
                    
                    # Validate grades data
                    grades_data = student_record.get('grades', {})
                    if not grades_data:
                        print(f"Skipping student {i+1}: No grades data")
                        continue
                    
                    is_valid, errors = generator.grade_validator.validate_grades_data(grades_data)
                    if not is_valid:
                        print(f"Skipping student {i+1}: Invalid grades - {'; '.join(errors)}")
                        continue
                    
                    # Format text templates
                    formatted_texts = generator.text_formatter.format_all_templates(combined_data, text_templates)
                    
                    # Generate filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{combined_data['student']['firstname']}_{combined_data['student']['name']}_transcript_{timestamp}_{i+1:03d}.pdf"
                    output_path = os.path.join(pdf_directory, filename)
                    
                    # Generate PDF
                    generator.pdf_generator.generate_transcript(
                        formatted_texts, combined_data, grades_data, output_path
                    )
                    
                    generated_files.append({
                        'filename': filename,
                        'student_name': f"{combined_data['student']['firstname']} {combined_data['student']['name']}",
                        'path': output_path
                    })
                
                except Exception as e:
                    print(f"Error processing student {i+1}: {str(e)}")
                    continue
            
            if not generated_files:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({'error': 'No valid transcripts could be generated'})
                }
            
            # Create ZIP file with all PDFs
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file_info in generated_files:
                    zip_file.write(file_info['path'], file_info['filename'])
            
            zip_buffer.seek(0)
            zip_content = zip_buffer.getvalue()
            zip_base64 = base64.b64encode(zip_content).decode('utf-8')
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_filename = f"transcripts_batch_{timestamp}.zip"
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({
                    'success': True,
                    'filename': zip_filename,
                    'zip_data': zip_base64,
                    'generated_count': len(generated_files),
                    'student_names': [f['student_name'] for f in generated_files]
                })
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': f'Internal server error: {str(e)}'})
        }


def parse_multipart_form_data(body, content_type):
    """
    Simplified multipart form data parser for binary data.
    """
    # Extract boundary from content type
    boundary = None
    for part in content_type.split(';'):
        if 'boundary=' in part:
            boundary = part.split('boundary=')[1].strip()
            break
    
    if not boundary:
        raise ValueError("No boundary found in multipart data")
    
    # Split by boundary
    parts = body.split(f'--{boundary}'.encode())
    form_data = {}
    
    for part in parts[1:-1]:  # Skip first empty part and last closing part
        if not part.strip():
            continue
        
        # Split headers and content
        header_end = part.find(b'\r\n\r\n')
        if header_end == -1:
            continue
        
        headers = part[:header_end].decode('utf-8')
        content = part[header_end + 4:].rstrip(b'\r\n')
        
        # Extract field name from Content-Disposition header
        name = None
        for line in headers.split('\r\n'):
            if 'Content-Disposition:' in line and 'name=' in line:
                name_part = line.split('name=')[1]
                name = name_part.split(';')[0].strip('"')
                break
        
        if name:
            # Check if this is a file field based on headers
            if 'filename=' in headers:
                # Binary file data
                form_data[name] = content
            else:
                # Text field
                form_data[name] = content.decode('utf-8')
    
    return form_data


# Vercel requires a default export for the handler
default = handler