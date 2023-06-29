package com.grass.game;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;

import java.util.List;

public class grass {
    int x,y,w,h;
    float rotation;
    Texture image = new Texture("grass.png");

    int picX = 31;
    int picY = 16;

    boolean affectedNeighbour;


    public grass(int spread){
        this.x = 100 + spread;
        this.y = 100;
        this.w = 5;
        this.h = 14;
        this.rotation = 0;
       // this.delta = 0;
        this.affectedNeighbour = false;
    }

    public void draw(Batch batch){
        batch.draw(image, this.x, this.y, 2.5f,-10,this.w,this.h,1,1,this.rotation, picX, picY, this.w,this.h,false,false);
    }




    public void alterRotation(String direction) {                            // Bends the grass (Note: -20 to 20 degrees is the range it will stay in).

            if (direction.equals("right") && this.rotation > -20) {
                this.rotation -= 6;

            } else if (direction.equals("left") && this.rotation < 20){
                this.rotation += 6;

            }
    }



    public void repairRotation() {            // Repairs the altered rotation. As it can go either left or right if have two statements here to determine which way it has bent, then it
        if (!this.affectedNeighbour) {
            if (this.rotation > 0) {             // repairs itself correctly.
                this.rotation--;
            } else if (this.rotation < 0) {
                this.rotation++;
            }
        }

    }

    public void delta(int delta, String direction) {
        this.affectedNeighbour = true;

        if (this.rotation > -10 && direction.equals("right")){ this.rotation -= delta;  }
        if (this.rotation < 10 && direction.equals("left")){ this.rotation += delta;  }
    }


    public void delta2(int delta, String direction) {
        this.affectedNeighbour = true;

        if (this.rotation > -5 && direction.equals("right")){ this.rotation -= delta;  }
        else if ( this.rotation < -10 ) { this.rotation += 5;  }


        if (this.rotation < 5 && direction.equals("left")){ this.rotation += delta;  }
        else if ( this.rotation > 10 ) { this.rotation -= 5; }
}



    public int getX() {return this.x;}
    public boolean getAffected() {return this.affectedNeighbour; }

    public void resetAffected(){ this.affectedNeighbour = false;}

}
