#! /bin/bash

PSQL="psql --username=freecodecamp --dbname=salon --tuples-only --no-align -c"

echo -e "\n~~~~~ MY SALON ~~~~~\n"

MAIN_MENU() {
    if [[ $1 ]]
    then 
        echo -e "\n$1"
    else 
        echo -e "Welcome to My Salon, how can I help you?\n"
    fi

    echo "$($PSQL "SELECT CONCAT(service_id, ') ', name) FROM services ORDER BY service_id")"

    read SERVICE_ID_SELECTED
    case $SERVICE_ID_SELECTED in
        1) SERVICE_MENU 1 ;;
        2) SERVICE_MENU 2 ;;
        3) SERVICE_MENU 3 ;;
        4) SERVICE_MENU 4 ;;
        5) SERVICE_MENU 5 ;;
        *) MAIN_MENU "I could not find that service. What would you like today?" ;;
    esac
}

SERVICE_MENU() {
    echo -e "\nWhat's your phone number?"
    
    read CUSTOMER_PHONE
    CUSTOMER_NAME="$($PSQL "SELECT name FROM customers WHERE phone = '$CUSTOMER_PHONE'")"
    if [[ -z $CUSTOMER_NAME ]]
    then 
        echo -e "\nI don't have a record for that phone number, what's your name?"
        read CUSTOMER_NAME
        $PSQL "INSERT INTO customers(phone, name) VALUES('$CUSTOMER_PHONE', '$CUSTOMER_NAME')"
    fi

    SERVICE_NAME="$($PSQL "SELECT name FROM services WHERE service_id = $1")"
    CUSTOMER_ID="$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")"
    
    echo -e "\nWhat time would you like your $SERVICE_NAME, $CUSTOMER_NAME?"

    read SERVICE_TIME
    $PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES($CUSTOMER_ID, $1, '$SERVICE_TIME')"

    echo -e "\nI have put you down for a $SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."
}

MAIN_MENU 

# 2026.11.18 17:29

# 这个项目从15:10做到17:29，做了两个小时二十分钟。