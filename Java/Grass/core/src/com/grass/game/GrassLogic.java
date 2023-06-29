package com.grass.game;

import java.util.List;

public class GrassLogic {
    float delta;
    float spread;

    float playerDistance;
    String rotationDirection;


    public GrassLogic(){}





    public void checkCollision(List<grass> checkGrass, float playersLocation){
        int index = 0;
        int delta = 20;

        for (grass check : checkGrass){

                playerDistance = playersLocation - (check.getX() + 2.5f);                    // difference between the current grass index during the loop & the player :)

                if (playerDistance < 6 && playerDistance > -6) {                 // 6 is the width of one strand of grass + the distance between each. Therefore, there will always be two strands that are being stepped on.
                    if (playerDistance < 0) {
                        rotationDirection = "right";
                    } else if (playerDistance > 0){
                        rotationDirection = "left";
                    }

                    check.alterRotation(rotationDirection);

                    if (index < 59) {              // FIRST NEIGHBOUR
                        if (rotationDirection.equals("right")){ checkGrass.get(index + 1).delta(5, rotationDirection); } }
                    if (index > 0) {
                        if (rotationDirection.equals("left")) { checkGrass.get(index - 1).delta(5, rotationDirection); } }


                    // SECOND NEIGHBOUR

                    if (index < 58) {
                       if (rotationDirection.equals("right")){ checkGrass.get(index + 2).delta2(5, rotationDirection); } }
                    if (index > 2) {
                       if (rotationDirection.equals("left")){ checkGrass.get(index - 2).delta2(5, rotationDirection); } }

                }
                else if (check.getX() != 0){ check.repairRotation(); }
            check.resetAffected();
            index++;
        }
    }

}

