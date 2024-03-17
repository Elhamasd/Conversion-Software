#!/usr/bin/python
import os
import sys
from distutils.dir_util import copy_tree
from jinja2 import Environment, FileSystemLoader, Template
import zipfile
import shutil
import argparse
import subprocess
import os
import time
import pypandoc
class Scorm():
    def __init__(self) -> None:
      pass
    


    def create_directories(self,dirName):
       
        # Create directory
        
        try:
            # Create target Directory
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ") 
        except FileExistsError:
            print("Directory " , dirName ,  " already exists")        
            exit(1)
        subDirName = dirName+'/res'
        
        # Create target directory & all intermediate directories if don't exists
        try:
            os.makedirs(subDirName)    
            print("Directory " , subDirName ,  " Created ")
        except FileExistsError:
            print("Directory " , subDirName ,  " already exists")  
        return subDirName


    def copy_files(self,dirName, static):
        
        
        fromDirectory = static
        toDirectory = dirName
        try:
          copy_tree(fromDirectory, toDirectory)
          print("Content Copied From " , fromDirectory ,"to", toDirectory,  " Successfully ") 
        except FileExistsError:
          print("Content Failed to Copy From " , fromDirectory ,"to", toDirectory,  "")  
          exit(1)
          

    def copy_resources(self,subDirName, resfiles):
       
        
        fromDirectory = resfiles
        toDirectory = subDirName
        try:
          copy_tree(fromDirectory, toDirectory)
          print("Content Copied From " , fromDirectory ,"to", toDirectory,  " Successfully ") 
        except FileExistsError:
          print("Content Failed to Copy From " , fromDirectory ,"to", toDirectory,  "")  
          exit(1)

    def resourcelist(self,resource_content):
       
        all_resources = os.listdir (resource_content)
        output = ["res/" + f for f in all_resources ]
        return output

    def jinja_template(self,dirName, htmlfile, all_resources, templatefile): 
      

        f = open(templatefile)
        
        mytext = f.read()
        template = Template(mytext)
        
        output = template.render(starting_resource = htmlfile, resourcelist =  all_resources, title=dirName)

        
        outfile = open(dirName +'/imsmanifest.xml', 'w')
        outfile.write(output)
        outfile.close()
       
        '''if not os.path.exists(str(dirName)+"res/assets"):
                    os.makedirs(str(dirName)+"/res/assets")
        if not os.path.exists(str(dirName)+"/res/css"):
                    os.makedirs(str(dirName)+"/res/css")
        if not os.path.exists(str(dirName)+"/res/js"):
                    os.makedirs(str(dirName)+"/res/js")'''

    #----------------------------
    #Zip folder to create scorm package
    #------------------------------

    def retrieve_file_paths(self,dirName):
        
        # setup file paths variable
        filePaths = []
        
        # Read all directory, subdirectories and file lists
        for root, directories, files in os.walk(dirName):
          for filename in files:
              # Create the full filepath by using os module.
              filePath = os.path.join(root, filename)
              filePaths.append(filePath)
              print("===============")
              print(filePaths)
              
        # return all paths
        return filePaths
    

    def zip_directory(self,dirName,dirname1):
       
        
      # Assign the name of the directory to zip
        dir_name = dirName
        
        # Call the function to retrieve all files and folders of the assigned directory

        #filePaths = self.retrieve_file_paths(dir_name)

        '''dir=os.getenv('LOCALAPPDATA')
          
        def is_file(path):
            return os.path.isfile(path)
        
        zip_file = zipfile.ZipFile(str(dir)+"\\"+dirname1+'.zip', 'w',zipfile.ZIP_DEFLATED)
        with zip_file:
          # writing each file one by one
          for file in filePaths:
            if is_file(file):
                zip_file.write(file)
            #zip_file.write(file)
              
          print(dir_name+'.zip file is created successfully!')'''
        
        def zip_dir(directory, zip_name):
            directory=str(directory)
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, directory)
                        print(arcname)
                        zipf.write(file_path, str(dirname1)+"//"+arcname)

        
        dir=os.getenv('LOCALAPPDATA')
        directory_to_zip = dir_name
        '''if not os.path.exists(str(dir)+"\\scorm"):
                    os.makedirs(str(dir)+"\\scorm")'''
        zip_file_name = str(dir)+"\\"+dirname1+'.zip'
        zip_dir(directory_to_zip, zip_file_name)



        

        
    def delete_directory(self,dirName):
        
        
        # delete directory
        dirName = dirName
        
        try:
            # Delete target Directory
            shutil.rmtree(dirName, ignore_errors=False, onerror=None)
            print("Directory " , dirName ,  " Deleted ") 
        except FileExistsError:
            print("Directory " , dirName ,  " Failed to Delete")     


    def convertMdToHtml(self,packagename,fileinput,fileoutput):
        

        subprocess.call(['pandoc', fileinput,'-o', fileoutput])
        #directory, filename = os.path.split(fileinput)

        #input_dir = directory
        #output_dir = fileoutput

        # Get a list of all Markdown files in the input directory
        

        # Convert each Markdown file to HTML using Pandoc
        file=open(fileoutput,"r",encoding="utf-8")
        output=file.read()
        dir=os.getenv('LOCALAPPDATA')
        print(str(dir)+"\\"+packagename+'\\'+packagename+"\\res\\js\\SCORM_API_wrapper.js")
        dmn=str(dir)+"\\"+packagename+'\\'+packagename+"\\res\\js\\SCORM_API_wrapper.js"
        print("***********************90")
        scorm_api_script = '<script src="{}"></script>'.format(dmn)
        header="""<!DOCTYPE html> 
        <html lang="en" dir="ltr">  
          <head> 
              <meta charset="UTF-8"> 
              <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
              <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no,minimal-ui"> 
          </head>  
          <body>"""
        output += scorm_api_script # Append the script tag to the end of the HTML 
        output +="""\n </body> 
        </html>"""
      
        with open(fileoutput, 'w', encoding='utf-8') as f:
              f.write(header)
              f.write(output)

        
        '''output = pypandoc.convert_file(fileinput, 'html', format='markdown', extra_args=['-t', 'slidy', '--self-contained'])
            
        with open(fileoutput, 'w', encoding='utf-8') as f:
                f.write(output)'''
            
    def convertMdToPdf(self,fileinput,fileoutput):
        
      
      '''try:
          subprocess.call(['pandoc', fileinput,
          '-t',  'beamer', '-V', 'theme:Warsaw',
          '--output='+fileoutput])
      except:'''
        
      '''p=subprocess.call(['pandoc','-s', fileinput,
        '-t',  'beamer', '--pdf-engine=xelatex', 
        '--output='+fileoutput])'''
      print("============")
      '''p = subprocess.Popen(['pandoc','-s', fileinput,
        '-t',  'beamer', '--pdf-engine=xelatex', 
        '--output='+fileoutput], stdout=subprocess.PIPE)'''
      p = subprocess.Popen(['pandoc', '-s', fileinput,
                      '-t', 'beamer', '--pdf-engine=xelatex',
                      '--output=' + fileoutput, '--from=markdown'], stdout=subprocess.PIPE)

      p = subprocess.Popen(['pandoc', '-s', fileinput], shell=False)
      time.sleep(15)
      '''p = subprocess.Popen(['pandoc', fileinput,
        '-o', fileoutput], stdout=subprocess.PIPE)'''
      #time.sleep(15)
      try:
        self.delete_directory(dirName =fileoutput)
      except:
        pass
      
      
     
      #pandoc -s greek.md = -t latex -o greek.pdf
         
         
    def convertMdToScorm(self,fileinputmd,fileoutputhtml,fileoutputpdf,packagename):
       self.convertMdToHtml(packagename,fileinputmd,fileoutputhtml)
      
       #self.convertMdToPdf(fileinputmd,fileoutputpdf)
       self.main(packagename,fileoutputhtml)
    def main(self,packagename,fileoutputhtml):
        
        #args = argumentParser()
        dirName=packagename#args.package_name
        htmlResource=fileoutputhtml#args.html_file_name
        dir=os.getenv('LOCALAPPDATA')
        

        subDirName = self.create_directories(str(dir)+"\\"+dirName)

        resource_content = str(dir)+"\\"+dirName + '/res/'
        
        self.copy_files(dirName = str(dir)+"\\"+dirName, static ='static/')
        
        self.copy_resources(subDirName = subDirName, resfiles = 'resources/')

        resources = self.resourcelist(resource_content)
      
        self.jinja_template(dirName = str(dir)+"\\"+dirName, htmlfile = 'res/' + htmlResource, 
                    all_resources =resources,
                    templatefile = "static/imsmanifest.xml")

        self.zip_directory(str(dir)+"\\"+dirName,dirName)
        
        self.delete_directory(dirName = str(dir)+"\\"+dirName)  

    
