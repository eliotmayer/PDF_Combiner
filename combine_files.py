
# Function to combine PDF files

def combine_files(pdf_folder):

    '''
    Input:  pdf_folder = folder path as a string with / at the end
    Output: Multi-line string with (1) output folder, (2) output file, (3) number of files found
    '''

    output_subfolder = "Combined"
    output_filename  = "Combined PDF Files.pdf"

    import os
    import glob
    import PyPDF2

    result=''

    # Create the output folder if needed
    output_folder = pdf_folder + "/" + output_subfolder
    try:     # Create output folder if it doesn't already exist
        os.mkdir(output_folder)
    except:  # Hopefully the only reason we came here is that the folder already existed
        pass
    # print( f"Output folder:  {output_folder}" )
    result = result + f"Output folder:  {output_folder}"
    result = result + f"\nOutput file:  {output_filename}"

    # Gather the names of all PDF files in the specified folder
    search_for = pdf_folder + "/*.pdf"
    # print( f"Search criteria:  {search_for}" )
    pdf_files = glob.glob(search_for, recursive=False)  # Appears to return sorted list, but that is not guaranteed
    pdf_files.sort()                                    # Sort list to be certain
    print ( f'Number of files found:  {len(pdf_files)}' )

    # Merge the PDF files
    problem_files = 0
    pdf_merge_obj = PyPDF2.PdfFileMerger(strict=True)
    # print ( f"PDF files: {pdf_files}")
    for f in pdf_files:
        b = f.split("\\")[-1]
        try:
            pdf_merge_obj.append( f, bookmark=b )
            print( "Added:  " + b )
        except:
            print( "UNABLE TO ADD FILE: " + b )
            problem_files += 1
        
    # Write the output file
    output_file = output_folder + "\\" + output_filename
    pdf_merge_obj.write(output_file)
    pdf_merge_obj.close()
    # print(f"Merge complete. See '{output_filename}' in Output folder.")
    result = result + f"\nNumber of Files Combined:  {len(pdf_files)-problem_files}"
    if problem_files > 0:
        result = result + f"\nUnable to add {problem_files} files.  See command window for details."

    return result, output_folder



    
'''
glob ideas for making search case insensitive
(though this does not appear to be necessary, at least in Windows 10)

https://stackoverflow.com/questions/8151300/ignore-case-in-glob-on-linux/10886685

Here is my non-recursive file search for Python with glob like behavior for Python 3.5+

# Eg: find_files('~/Downloads', '*.Xls', ignore_case=True)
def find_files(path: str, glob_pat: str, ignore_case: bool = False):
    rule = re.compile(fnmatch.translate(glob_pat), re.IGNORECASE) if ignore_case \
            else re.compile(fnmatch.translate(glob_pat))
    return [n for n in os.listdir(os.path.expanduser(path)) if rule.match(n)]


Another idea from the same page: change pdf to [pP][dD][fF]

'''