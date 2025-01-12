# Cartoonify Image with OpenCV in Python

This project is a simple Cartoonify Image Generator built using Tkinter, NumPy, Matplotlib, and OpenCV. The application allows users to upload an image, apply cartoonification effects, and display the result in a graphical user interface (GUI).

Features
Image Upload: Select an image from your system using a file dialog.
Cartoonify Effect: Apply a cartoon effect to the image.
Display Results: View the cartoonified image in the app window.
Save Output: Option to save the cartoonified image to your local machine.
Libraries Used
Tkinter: Used for creating the graphical user interface (GUI).
NumPy: Used for efficient numerical operations on image data.
Matplotlib: Used for displaying the images in the GUI.
OpenCV: Used for the image processing tasks (reading, blurring, edge detection, etc.).

How It Works
Image Upload: The user selects an image through a file dialog using Tkinter.
Cartoonification Process:
The image is loaded using OpenCV.
A smoothing filter (e.g., bilateral filter) is applied to reduce the color palette of the image, giving it a smooth, cartoonish appearance.
Edge detection is applied to highlight the contours of the image.
The edges are blended with the smoothed image to create the cartoon effect.
Display: The cartoonified image is displayed within the Tkinter window using Matplotlib.
Save: Users can save the cartoonified image to their local directory.
Installation
To run this project, you need to have Python and the necessary libraries installed. Follow the steps below:

Step 1: Clone the repository
bash
Copy code
git clone https://github.com/yourusername/cartoonify-image-generator.git
cd cartoonify-image-generator
Step 2: Install required libraries
You can install the required libraries using pip. Run the following command:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file includes the following libraries:

opencv-python
numpy
matplotlib
tkinter
Note: tkinter is usually included with Python, but if it's not, you can install it separately based on your operating system.

Step 3: Run the Application
Once the required libraries are installed, you can run the application with the following command:

bash
Copy code
python cartoonify_app.py
This will open the Tkinter window where you can upload an image, apply the cartoon effect, and view/save the result.

Contributing
Feel free to fork this project, report issues, or submit pull requests. Contributions are always welcome!
