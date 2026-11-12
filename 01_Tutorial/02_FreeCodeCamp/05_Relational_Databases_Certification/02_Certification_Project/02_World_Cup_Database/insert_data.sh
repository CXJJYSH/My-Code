#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

cat games.csv | while read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
    $($PSQL "INSERT INTO games(year, round, winner_goals, opponent_goals) VALUES($YEAR, '$ROUND', $WINNER_GOALS, $OPPONENT_GOALS)")
done
