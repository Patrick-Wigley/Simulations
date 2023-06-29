package com.grass.game;

import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.Rectangle;

public class Player {
    float x, y, w, h;

   //ShapeRenderer shapeRenderer = new ShapeRenderer();   // messing up


    public Player() {
        this.x = 200;
        this.y = 100;
        this.w = 10;
        this.h = 30;
    }

    public void draw(ShapeRenderer shapeRenderer) {
        shapeRenderer.begin((ShapeRenderer.ShapeType.Filled));
        shapeRenderer.rect(this.x + 2.5f, this.y, this.w - 2.5f, this.h);
        shapeRenderer.end();
    }

    public void move(float speed, String direction) {
        this.x += speed;
    }


    public float getX() {return this.x;}


}
