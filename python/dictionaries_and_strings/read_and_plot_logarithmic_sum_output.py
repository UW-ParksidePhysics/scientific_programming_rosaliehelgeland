import numpy as np 
import matplotlib.pyplot as plt 

def parse_animation_code(code_filename):
    with open(code_filename, 'r') as File:
        code = File.read()

    preformatted_start = "<pre>"
    preformatted_end = "</pre>"

    return preformatted_start + code + preformatted_end

def format_section_header(header_string):
    header_one_start = "<h1>"
    header_one_end = "</h1>"

    return header_one_start + header_string _ header_one_end

def write_html_report(report_string, report_filename):
    with open(report_filename, "w") as File:
        File.write(report_string)