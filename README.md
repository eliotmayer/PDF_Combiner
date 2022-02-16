# PDF_Combiner

This Python program combines all PDF files in a folder into a single PDF file.

The simple GUI was built with tkinter.  The PDF combination is done with the PyPDF2 module.

File build_pdf_combiner.txt describes my learning curve with pyinstaller.

One or more exectuble versions of the program, created with pyinstaller, are in the "dist" sub-folder.  These are for the Windows operating system, tested on Windows 10.

## Usage

1.  Start the app.
2.  Click "Select Folder" and select the fold of PDF files to be combined.
3.  Click "Combine Files" to combine the files into a single PDF in the Combined sub-folder.
4.  Optionally, click "Open Output Folder" to open File Explorer to the Combined sub-folder.

Status is reported.  As shown below, the app reports on any corrupted PDF files that could not be added.

![image](https://user-images.githubusercontent.com/99143745/154312374-8361dca7-5572-4bd7-ae57-a0400aa2ba88.png)

![image](https://user-images.githubusercontent.com/99143745/154312430-c2c62c83-3d1b-42d5-8370-ab378cf47441.png)

![image](https://user-images.githubusercontent.com/99143745/154312586-6c7ebb14-4ff1-42b2-843d-c3bc20236759.png)

The output file, "Combined PDF Files.pdf", contains Bookmarks with the names of the original files.
