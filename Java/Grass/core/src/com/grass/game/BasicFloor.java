package com.grass.game;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

public class BasicFloor {
    int x,y,w,h;


    ShapeRenderer shapeRenderer = new ShapeRenderer();

    public BasicFloor(int spacing){   // Y = 405
        this.x = 50 + spacing;
        this.y = 80;
        this.w = 20;
        this.h = 20;
    }

    public void draw(){
     //   shapeRenderer.setProjectionMatrix(camera.combined);
        shapeRenderer.begin(ShapeRenderer.ShapeType.Line);
        shapeRenderer.rect(this.x, this.y, this.w, this.h);
        shapeRenderer.end();
    }
}
