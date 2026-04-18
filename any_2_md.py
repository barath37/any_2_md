import os
import warnings
import subprocess
from markitdown import MarkItDown

# Ignore the ffmpeg warning
warnings.filterwarnings("ignore", category=RuntimeWarning, module='pydub')

def main():
    md = MarkItDown()
    
    print(r"Example Input: D:\barath\College\Resume.pdf")
    path = input("Paste/Drag source file here: ").strip().strip('"')
    
    if os.path.exists(path):
        # 1. Set the fixed output location and filename
        output_file = r"D:\barath\coding\Projects\Any 2 MD\output.md"
        
        print(f"Converting: {os.path.basename(path)}...")
        
        try:
            result = md.convert(path)
            
            # 2. Write/Overwrite the fixed output.md file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(result.text_content)
                
            print(f"✅ Success! Created: {output_file}")

            # 3. Automatically open the file with the default system app
            os.startfile(output_file)
            
        except Exception as e:
            print(f"❌ Error during conversion: {e}")
    else:
        print(f"❌ File not found at: {path}")

if __name__ == "__main__":
    main()
