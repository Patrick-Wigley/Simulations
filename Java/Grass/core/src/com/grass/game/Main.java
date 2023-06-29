package com.grass.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

import java.util.ArrayList;
import java.util.List;

public class Main extends ApplicationAdapter {
	List<grass> grasses = new ArrayList<>();
	List<BasicFloor> floors = new ArrayList<>();
	GrassLogic grassMain = new GrassLogic();

	int spread = 0;

	private SpriteBatch batch;
	private Player player;
	ShapeRenderer shapeRenderer;
	Texture background;

	public float speed = 0;
	public float sprint = 0;
	public String direction = "right";



	@Override
	public void create () {
		batch = new SpriteBatch();
		shapeRenderer = new ShapeRenderer();
		player = new Player();
		background = new Texture("background.png");

		spread = 0;
		for (int i = 0; i < 23; i++){
			floors.add(new BasicFloor(spread));
			spread += 20;
		}

		spread = 0;
		for (int i = 0; i < 60; i++){
			grasses.add(new grass(spread));
			spread += 4;
		}

	}

	@Override
	public void render () {
		update();



		batch.begin();
		batch.draw(background, 0,0);

		for (grass draw : grasses){
			draw.draw(batch);
		}

		batch.end();
		for (BasicFloor draw : floors){
			draw.draw();
		}


		player.draw(shapeRenderer);
	}
	
	@Override
	public void dispose () {
		//batch.dispose();
	}

	private void keyDetection(){
		speed = 0;
		sprint = 0;

		if ( Gdx.input.isKeyPressed((Input.Keys.SHIFT_LEFT))){
			sprint = 1;
		}

		if (Gdx.input.isKeyPressed(Input.Keys.D) || Gdx.input.isKeyPressed(Input.Keys.RIGHT)) {
			speed = .5f + sprint;
			direction = "right";

		}
		else if (Gdx.input.isKeyPressed((Input.Keys.A)) || Gdx.input.isKeyPressed(Input.Keys.LEFT)){
			speed = -.5f - sprint;
			direction = "left";

		}
	}

	private void update(){
		keyDetection();
		player.move(speed, direction);
		grassMain.checkCollision(grasses, player.getX() +5 );


	}
}
