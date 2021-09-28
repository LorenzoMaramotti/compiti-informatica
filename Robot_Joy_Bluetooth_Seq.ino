#include <Servo.h>  //add Servo library files
Servo myservo1;  // create servo object to control a servo
Servo myservo2;
Servo myservo3;
Servo myservo4;

//Constant for hardware association
const int rotation = A1;  //Define the servo rotation pin to A1
const int left_side = A0;  //Define the servo left side pin to A0
const int right_side = 8;  //Define the servo right side pin to 8
const int clamp = 9;  //Define the servo clamp pin to 9
const int right_X = A2; // define the right X pin to A2
const int right_Y = A5; //define the right Y pin to A5
const int right_key = 7; // define the right key to 7(the value of Z axis)
const int left_X = A3; // define the left X pin to A3
const int left_Y = A4;  // define the left Y pin to A4
const int left_key = 6; // define the left key to 6(the value of Z axis)
const int filter_Button = 500; // debounce filter

int x1,y1,z1;   //define a variable to store the read right Joystick value
int x2,y2,z2;   //define a variable to store the read left Joystick value
int mode;
int seq;
int pos1=90, pos2=60, pos3=90, pos4=0;  // define the variables of 4 Servo angle and assign initial values(posture angle values of boot-up)
int pos1_ll=1, pos1_ul=180; //limit position for rotation servo
int pos2_ll=30, pos2_ul=135; //limit position for left servo
int pos3_ll=45, pos3_ul=160; //limit position for right servo
int pos4_ll=0, pos4_ul=100; //limit position for clamp servo

int save_pos1[10];  //define 4 array, separately save the angle of 4 Servo
int save_pos2[10];  //（array length is 10，namely can save angle data of 0~10 servo ）
int save_pos3[10];  //if need to save more data, just change the number 10 to be more larger number.
int save_pos4[10];
int i=0; //for looping
int j=0; //for saving the last value of “i”

int execute=0;

int old_z1,old_z2;
int z1_pr,z2_pr;
int old_z1_pr,old_z2_pr;
int z1_time,z2_time;
int len;

char val;

void setup()
{
  Serial.begin(9600); //  set baud rate to 9600

  myservo1.attach(rotation);  //set control pin of servo1 to A1
  myservo2.attach(left_side);  //set control pin of servo2 to A0
  myservo3.attach(right_side);   //set control pin of servo3 to D8
  myservo4.attach(clamp);   //set control pin of servo4 to D9

  z2 = digitalRead(left_key);  //read the value of left Z axis

  if (z2>0)
  {
    mode=1;
  }
  else
  {
    mode=0;
  }

  Serial.println(mode);
  
   //posture of boot-up
  myservo1.write(pos1);  
  myservo2.write(pos2);
  myservo3.write(pos3);
  myservo4.write(pos4);
  delay(1500);
  //mode=1;
  //load_default_path();
}

void loop() 
{ 
   if (mode==0)
  { 
     if(Serial.available())   //determine if data is received
    {
      len=Serial.available();
      val=Serial.read();    //read the received data
      Serial.print(val);
      Serial.print("  ");
      Serial.println(len);
      z1=0;
      z2=0;
    }
    switch(val)   
      {
        case 'L':  arm_open();  break;   //claw opens
        case 'R':  arm_close();  break;   //claw closes
        case 'B':  left_f();  break;   //left servo swings forward
        case 'F':  left_b();  break;   //left servo swings back ward
        case 'f':  right_f();  break;   //right servo stretches out
        case 'b':  right_b();  break;   //right servo draws back
        case 'l':  R_left();  break;  //base servo turns left
        case 'r':  R_right();  break;  //base servo turns right
        case 'q':  z2=1 ;  break;  //base servo turns right
        //case 'r':  R_right();  break;  //base servo turns right
        
      }
  }
  else
  //Joystick control pprocessing
    {
    //Joystick devides reading 
    x1 = analogRead(right_X); // read the value of right X axis
    y1 = analogRead(right_Y);  // read the value of right Y axis
    z1 = digitalRead(right_key);  ////read the value of right Z axis
    x2 = analogRead(left_X);  //read the value of left X axis
    y2 = analogRead(left_Y);  //read the value of left Y axis
    z2 = digitalRead(left_key);  //read the value of left Z axis
    
    //Rotation command
    if(x1<50)  // if push the left joystick to the right
      {
      R_right();
      }
    if(x1>1000)  // if push the left joystick to the right
      {
      R_left();
      }
      
    //Right servo command
    if(y1<50)  // if push the left joystick to the right
      {
      right_f();
      }
    if(y1>1000)  // if push the left joystick to the right
      {
      right_b();
      }
      
    //Left servo command
    if(y2>1000)  // if push the left joystick to the right
      {
      left_f();
      }
    if(y2<50)  // if push the left joystick to the right
      {
      left_b();
      }
      
    //Clamp servo command
    if(x2<50)  // if push the left joystick to the right
      {
      arm_close();
      }
    if(x2>1000)  // if push the left joystick to the right
      {
      arm_open();
      }
    }

//Debounce Z1 button
  if (z1>0)
    {
      if (old_z1==0)
        {
          old_z1=1;
          z1_time=millis();
        }
       else
        {
          if((millis()-z1_time)>filter_Button)
            {
              z1_pr=1;
              //Serial.println("Z1 Pressed");
            } 
         }
      }
    else
    {
      old_z1=0;
      z1_pr=0;
      //Serial.println("Z1 Not Pressed");
    }
    
//Debounce Z2 button
if (z2>0)
    {
      if (old_z2==0)
        {
          old_z2=1;
          z2_time=millis();
        }
       else
        {
          if((millis()-z2_time)>filter_Button)
            {
              z2_pr=1;
              //Serial.println("Z2 Pressed");
            } 
         }
      }
    else
    {
      old_z2=0;
      z2_pr=0;
      //Serial.println("Z1 Not Pressed");
    }

// point acquisition
if (z2_pr==1)
   { 
    if (old_z2_pr==0)
     { 
      add_point();
      old_z2_pr=1;
    }
   }
else
   { 
      old_z2_pr=0;
   }

//Point execution

if (z1_pr==1)
   { 
    if (old_z1_pr==0)
     {
      if (execute==0)
        {
          execute=1;
          Serial.println("Execute On");     
        }
      else
        {
          execute=0;
          Serial.println("Execute Off");
        }
      ;
      old_z1_pr=1;
    }
   }
else
   { 
      old_z1_pr=0;
   }

//Cyclce execution management

if (execute==1)
  {
  execute_point();  
        Serial.println("Execute Point");
  }

} 

//**************************************************

void execute_point()
{
  myservo1.write(save_pos1[i]);  
  myservo2.write(save_pos2[i]);
  myservo3.write(save_pos3[i]);
  myservo4.write(save_pos4[i]);

  Serial.print("Execute point : ");
  Serial.print(i);
  Serial.print(" Pos 1 : ");
  Serial.print(save_pos1[i]);
  Serial.print(" Pos 2 : ");
  Serial.print(save_pos2[i]);
  Serial.print(" Pos 3 : ");
  Serial.print(save_pos3[i]);
  Serial.print(" Pos 4 : ");
  Serial.println(save_pos4[i]);
  
  delay(500);
  i=i+1;
  if (i>=j)
   {
     i=0;
   }
  }  


void add_point()
{
if (j<10)
  {
  save_pos1[j]=pos1;  //define 4 array, separately save the angle of 4 Servo
  save_pos2[j]=pos2;  //（array length is 10，namely can save angle data of 0~10 servo ）
  save_pos3[j]=pos3;  //if need to save more data, just change the number 10 to be more larger number.
  save_pos4[j]=pos4;
  
  Serial.print("Save point : ");
  Serial.print(j);
  Serial.print(" Pos 1 : ");
  Serial.print(pos1);
  Serial.print(" Pos 2 : ");
  Serial.print(pos2);
  Serial.print(" Pos 3 : ");
  Serial.print(pos3);
  Serial.print(" Pos 4 : ");
  Serial.println(pos4);
 
  j=j+1; 
  }
    
}


void load_default_path()
{
j=8;

save_pos1[0]=1,save_pos2[0]=60,save_pos3[0]=90,save_pos4[0]=100; 
save_pos1[1]=1,save_pos2[1]=60,save_pos3[1]=90,save_pos4[1]=0; 
save_pos1[2]=1,save_pos2[2]=120,save_pos3[2]=45,save_pos4[2]=0; 
save_pos1[3]=180,save_pos2[3]=120,save_pos3[3]=45,save_pos4[3]=0; 
save_pos1[4]=180,save_pos2[4]=51,save_pos3[4]=125,save_pos4[4]=0; 
save_pos1[5]=180,save_pos2[5]=51,save_pos3[5]=125,save_pos4[5]=100; 
save_pos1[6]=180,save_pos2[6]=120,save_pos3[6]=45,save_pos4[6]=100; 
save_pos1[7]=1,save_pos2[7]=120,save_pos3[7]=45,save_pos4[7]=100; 

}


//Rotation left
void R_left()
{
    pos1=pos1+1;
    myservo1.write(pos1);
    delay(6);
    if(pos1>pos1_ul)
    {
      pos1=pos1_ul;
    }
}
//Rotation right
void R_right()
{
    pos1=pos1-1;
    myservo1.write(pos1);
    delay(6);
    if(pos1<pos1_ll)
    {
      pos1=pos1_ll;
    }
}
//********************************************
//clamp closes
void arm_close()
{
      pos4=pos4-1;
      myservo4.write(pos4);
      delay(2);
      if(pos4<pos4_ll)
      {
        pos4=pos4_ll;
      }
}
//clamp opens
void arm_open()
{
    pos4=pos4+1;
      myservo4.write(pos4);
      delay(2);
      if(pos4>pos4_ul)
      {
        pos4=pos4_ul;
      }
}

//******************************************
//left servo forward
void left_f()
{
    pos2=pos2-1;
    myservo2.write(pos2);
    delay(8);
    if(pos2<pos2_ll)
    {
      pos2=pos2_ll;
    }
}
//left servo backward
void left_b()
{
    pos2=pos2+1;
    myservo2.write(pos2);
    delay(8);
    if(pos2>pos2_ul)
    {
      pos2=pos2_ul;
    }
}

//***************************************
//right servo forward
void right_f()
{
  pos3=pos3+1;
    myservo3.write(pos3);
    delay(8);
    if(pos3>pos3_ul)
    {
      pos3=pos3_ul;
    }
}
//right servo backward
void right_b()
{
  pos3=pos3-1;
    myservo3.write(pos3);
    delay(8);
    if(pos3<pos3_ll)
    {
      pos3=pos3_ll;
    }
}
