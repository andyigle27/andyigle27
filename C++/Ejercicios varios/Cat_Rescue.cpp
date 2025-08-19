#include <iostream>
#include <string>

class Cat {
  public:
   std::string name;
   std::string breed;
   int age, mood, hunger;
   bool rescued;
   Cat(std::string n, std::string b, int a, bool r, int m, int h){
     name = n;
     breed = b;
     age = a;
     rescued = r;
     mood = m;
     hunger = h;
   }
   int feed(int food){
     hunger = hunger +food;
     return hunger;
   }
   int play(int toy){
     mood = mood +toy;
     return mood;
   }
   void display_status(){
     std::cout<< "Name: "<<name<<"\n";
     std::cout<< "Breed: "<<breed<<"\n";
     std::cout<< "Age: "<<age<<"\n";
     if(rescued==true){
       std::cout<< "Rescatado\n";
     }else if(rescued==false){
       std::cout<< "No rescatado\n";
     }
     std::cout<< "Mood: "<<mood<<"\n";
     std::cout<< "Hunger: "<<hunger;
   }


};

int main() {
  // Write code here 💖
  int op1, op2;
  Cat cat1("Tom","Gris",5, true, 4, 10 );
  Cat cat2("Kitty", "Blanco", 1, false, 10, 2);
  Cat cat3("Garfield", "Naranja",50, false, 1,  1 );
  std::cout<< "Which cat would you like to see?\n";
  std::cout<< "1) Tom  2) Kitty  3) Garfield\n->";
  std::cin>> op1;
  std::cout<< "What would you like to do?\n";
  std::cout<< "1) Feed  2) Play  3) Check status\n->";
  std::cin>> op2;
  if(op1==1){
    if (op2==1){
      cat1.feed(1);
      cat1.display_status();
    } else if(op2==2){
      cat1.play(1);
      cat1.display_status();
    }else if(op2==3){
      cat1.display_status();
    }
  } else if(op1==2){
    if (op2==1){
      cat2.feed(1);
      cat2.display_status();
    } else if(op2==2){
      cat2.play(1);
      cat2.display_status();
    }else if(op2==3){
      cat2.display_status();
    }
  } else if (op1==3){
    if (op2==1){
      cat3.feed(1);
      cat3.display_status();
    } else if(op2==2){
      cat3.play(1);
      cat3.display_status();
    }else if(op2==3){
      cat3.display_status();
    }
  }
}