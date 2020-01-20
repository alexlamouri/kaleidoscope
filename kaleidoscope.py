import turtle as t
import random
import time
import os


# ---------------------------SHAPE FUNCTIONS-------------------------------------


# Draw Basic Square
def draw_square(side, color):
    '''
    Draw a basic square with given side and color
    
    PARAMETERS
    side: int
    color: string
    
    RETURN
    void
    '''
    
    t.pencolor("black")
    t.fillcolor(color)
    t.begin_fill()
    # Draw one side four times
    for i in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()


# Draw Basic Circle
def draw_circle(radius, color):
    '''
    Draw a basic circle with given radius and color
    
    PARAMETERS
    radius: int
    color: string
    
    RETURN
    void
    '''
    
    # Center circle
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()
    
    # Draw circle
    t.pencolor("black")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
    # Return to circle
    t.penup()
    t.home()


# Draw Complex square
def draw_complex_square(num_layers, num_squares, largest_side):
    '''
    Draw num_layers layers of num_squares squares of different colors
    
    PARAMETERS
    num_layers: int
    num_squares: int
    largest_side: int
    
    RETURN
    void
    '''

    side = largest_side
    
    # Spacing between each layer
    spacing = side / num_layers
    
    # Angle between each square
    angle = 360 / num_squares
    
    for i in range(num_layers):
       
        for j in range(num_squares):
            # Generate random color
            r = random.random()
            g = random.random()
            b = random.random()
            color = (r,g,b)
            
            draw_square(side, color)
           
            t.penup()
            t.left(angle)
            t.pendown()
        
        # Adjust side length for next layer
        side -= spacing   
      
      
# Draw Complex Circle 
def draw_complex_circle(num_circles, largest_radius):
    '''
    Draw num_circles concentric circles of different colors
    
    PARAMETERS
    num_circles: int
    largest_radius: int
    
    RETURN
    void
    '''
    
    radius = largest_radius
    
    # Spacing between each layer (circle)
    spacing = radius / num_circles  
       
    for j in range(num_circles):
        # Generate random color
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r,g,b)
        
        draw_circle(radius, color)

        # Adjust radius for next layer (circle)
        radius -= spacing
        
        
# --------------------------------MAIN------------------------------------------


# Paint Instructions
print("---------------------------------------------------------------")
print("Welcome to the CCT111 Paint Program powered by Turtle Graphics")
print("---------------------------------------------------------------")


valid_mode = False
while not valid_mode:
    
    
    # Prompt user for input : mode
    selection = input("Please select a mode [SQUARE/CIRCLE]: ").upper()
    
    
    # Square Mode
    if selection == "SQUARE":
        valid_mode = True
        print("---------------------")
        print("SQUARE MODE SELECTED")
        print("---------------------")        
        
        print("This program draws multiple layers of multiple squares of different colors\n")
        
        
        # square : num_layers
        valid_num = False
        while not valid_num:
            
            # Prompt user for input
            num_layers_str = input("Enter a number of layers: ")
            
            # Check in input is of type int
            if num_layers_str.isdigit():
                
                # Convert str to int
                num_layers_int = int(num_layers_str)
                
                # Check if int >= 1
                if num_layers_int >= 1:
                    valid_num = True
                    
                else:
                    print("VALUE ERROR :  Please enter an integer  >= 1\n")
                
            else: 
                print("FORMAT ERROR : Please enter a number in integer format\n")            
                
                
        # square : num_squares
        valid_num = False
        while not valid_num:
                    
            # Prompt user for input
            num_squares_str = input("Enter a number of squares per layer: ")
            
            # Check in input is of type int
            if num_squares_str.isdigit():
                
                # Convert str to int
                num_squares_int = int(num_squares_str)
                
                # Check if int >= 1
                if num_squares_int >= 1:
                    valid_num = True
                    
                else:
                    print("VALUE ERROR :  Please enter an integer  >= 1\n")
                
                
            else: 
                print("FORMAT ERROR : Please enter a number in integer format\n") 
               
               
        # square : largest_side
        valid_num = False
        while not valid_num:
                    
            # Prompt user for input
            largest_side_str = input("Enter the side length of the largest square: ")
            
            # Check if input is of type int
            if largest_side_str.isdigit():
                
                # Convert str to int
                largest_side_int = int(largest_side_str)
                
                # Check if int >= 1
                if largest_side_int >= 1:
                    valid_num = True
                    
                else:
                    print("VALUE ERROR :  Please enter an integer >= 1\n")
                
                
            else: 
                print("FORMAT ERROR : Please enter a number in integer format\n")          
                
                
        # Draw Complex Square with given parameters from user input
        draw_complex_square(num_layers_int, num_squares_int, largest_side_int)  
        
        
    # Circle Mode
    elif selection == "CIRCLE":
        valid_mode = True
        print("---------------------")
        print("CIRCLE MODE SELECTED")
        print("---------------------")    
        
        print("This program draws multiple layers of circles of different colors\n")
                
                
        # circle : num_circles
        valid_num = False
        while not valid_num:
                    
            # Prompt user for input
            num_circles_str = input("Enter a number of circles: ")
            
            # Check if input is of type int
            if num_circles_str.isdigit():
                
                # Convert str to int
                num_circles_int = int(num_circles_str)
                
                # Check if int >= 1
                if num_circles_int >= 1:
                    valid_num = True
                    
                else:
                    print("VALUE ERROR :  Please enter an integer >= 1\n")
                
            else: 
                print("FORMAT ERROR : Please enter a number in integer format\n")      
        
        
        # circle : largest_radius     
        valid_num = False
        while not valid_num:
                    
            # Prompt user for input
            largest_radius_str = input("Enter the radius of the largest circle: ")
            
            # Check if input is of type int
            if largest_radius_str.isdigit():
                
                # Convert str to int
                largest_radius_int = int(largest_radius_str)
                
                # Check if int >= 1
                if largest_radius_int >= 1:
                    valid_num = True
                    
                else:
                    print("VALUE ERROR :  Please enter an integer >= 1\n")
                
            else: 
                print("FORMAT ERROR : Please enter a number in integer format\n")                                      
                
        # Draw Complex Circle with given parameters from user input
        draw_complex_circle(num_circles_int, largest_radius_int)  
                        
    else: 
        print("Incorrect mode selection. Please select between [SQUARE/CIRCLE]\n")
      
        
# Pause 5 seconds after drawing is complete      
time.sleep(5)

# Exit Turtle program
os._exit(1)