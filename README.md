# lab2.3D-house

This code is a Python script that uses a library called Cairo to draw a 2D representation of a house with a mirror effect. Here's a step-by-step breakdown of what the code does:

## Setting Up the Drawing Area
   - The code starts by creating an area where the drawing will happen, called a "surface." Think of it like a blank canvas where the house will be painted. The surface is 800 pixels wide and 600 pixels tall. The background is filled with white color.

2. **Mirroring the Image**:
   After the house is drawn, the code mirrors the image along the vertical axis (left to right). This means whatever is drawn on the left side will be reflected on the right side, creating a symmetric effect. This is done using a technique called "translation" and "scaling."

3. **Drawing the Main House**: 
   The code then draws the main part of the house. This includes the front walls and side walls. The walls are drawn using lines that form rectangles, and they are colored in light beige with darker outlines.

4. **Drawing the Roof**:
   Next, the roof is drawn. It has two parts: the front and the side. The roof is drawn as a triangle with sharp edges and filled with a red-orange color, making it look like a slanted roof.

5. **Adding Windows**:
   The house has windows on the front and side. The windows are drawn as rectangles, with each one divided into smaller sections, giving the appearance of window panes. The windows are filled with a light blue color to make them look like glass.

6. **Adding a Dormer Window**:
   There's also a small window on the roof, called a dormer. This dormer has its own little roof and window, and it is drawn similarly to the main house windows but in a smaller, more triangular shape.

7. **Drawing the Door**:
   The house also has a door at the bottom of the front wall. The door is a rectangle with a round handle on it. The door is colored in a wooden brown tone.

8. **Saving the Image**:
   Finally, after all these parts are drawn, the image is saved as a PNG file (a type of picture file) named "3d_house_mirrored.png." This file can be opened to view the house.

### In Summary:
This code draws a simple 2D house, adds details like windows, a door, a roof, and a dormer, and then creates a mirrored version of the house on the right side of the image. The final result is saved as a picture file.
