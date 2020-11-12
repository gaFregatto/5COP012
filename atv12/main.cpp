#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <GL/glut.h>

#define PI 3.1415926535897932384626433832795

void init(){
    glClearColor(1, 1, 1, 1); 
        
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(-1, 1, -1, 1);
}


void display(){
    float radius = 0.3;
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    // Draw green rectangle
    glColor3f(0, 0.57, 0.24);
    glBegin(GL_POLYGON);    
        glVertex2f(-0.9, -0.6);
        glVertex2f(-0.9, 0.6);        
        glVertex2f(0.9, 0.6);
        glVertex2f(0.9, -0.6);
    glEnd();

    // Rectangle contour
    glColor3f(0, 0, 0);
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.9, -0.6);
        glVertex2f(-0.9, 0.6);        
        glVertex2f(0.9, 0.6);
        glVertex2f(0.9, -0.6);
    glEnd();

    // Draw yellow diamond
    glColor3f(0.97, 0.75, 0);
    glRotatef(45,0,0,1);
    glBegin(GL_POLYGON);    
        glVertex2f(-0.35, -0.35);
        glVertex2f(-0.55, 0.55);        
        glVertex2f(0.35, 0.35);
        glVertex2f(0.55, -0.55);
    glEnd();

    // Diamond contour
    glColor3f(0, 0, 0);
    glLineWidth(1.5);
    glBegin(GL_LINE_LOOP);
        glVertex2f(-0.35, -0.35);
        glVertex2f(-0.55, 0.55);        
        glVertex2f(0.35, 0.35);
        glVertex2f(0.55, -0.55);
    glEnd();

    // Draw blue circle
    glColor3f(0.15, 0.08, 0.43);
    glBegin(GL_POLYGON);    
        for(float i=0; i<2*PI; i+=PI/48)
            glVertex2f(cos(i) * radius, sin(i) * radius);
    glEnd();

    // Circle contour
    glColor3f(0, 0, 0);
    glLineWidth(1.5);
    glBegin(GL_LINE_LOOP);
        for(float i=0; i<2*PI; i+=PI/48)
            glVertex2f(cos(i) * radius, sin(i) * radius);
    glEnd();

    glFlush();
}


int main(int argc, char *argv[]){

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB); 
    glutInitWindowSize(600, 600); 
    glutInitWindowPosition(100, 50); 
    glutCreateWindow("OpenGL Application");
    init(); 
    glutDisplayFunc(display); 
    glutMainLoop(); 

    return 0;
}