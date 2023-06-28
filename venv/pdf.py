import os
from selenium import webdriver
from fpdf import FPDF
from selenium.webdriver.common.by import By
import time



pdf= FPDF("P","mm","Letter")
pdf.add_page()
pdf.set_font('helvetica', '' ,16)
pdf.cell(40,10,'Hello World')
pdf.cell(40,10,'Hello World')
pdf.cell(40,10,'Hello World')


#pdf.text("HEllo world this is invozone")
pdf.output("dummy.pdf")
#driver = webdriver.Chrome(executable_path='/Users/maham-basharat/Downloads/chromedriver')
#driver.maximize_window();