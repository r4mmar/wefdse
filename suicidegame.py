#!/bin/bash

echo "🎮 Welcome to Real Squid Game: Rock, Paper, Scissors!"
echo -e "💡 You have 3 lives. Lose them all... and it's over. 💀\n"

choices=("rock" "paper" "scissors")
lives=3
score=0

while [ $lives -gt 0 ]; do
    echo "❤ Lives: $lives | 🏆 Score: $score"
    read -p "Choose (rock, paper, scissors): " player_choice
    # Ubah input menjadi huruf kecil
    player_choice=$(echo "$player_choice" | tr '[:upper:]' '[:lower:]')

    # Validasi input
    if [[ ! " ${choices[@]} " =~ " ${player_choice} " ]]; then
        echo -e "❌ Invalid input. Try again.\n"
        continue
    fi

    # Komputer memilih secara acak
    computer_choice=${choices[$RANDOM % 3]}
    echo "🤖 Computer chose: $computer_choice"

    # Logika menang/kalah/seri
    if [ "$player_choice" == "$computer_choice" ]; then
        echo -e "🤝 It's a tie!\n"
    elif { [ "$player_choice" == "rock" ] && [ "$computer_choice" == "scissors" ]; } || \
         { [ "$player_choice" == "paper" ] && [ "$computer_choice" == "rock" ]; } || \
         { [ "$player_choice" == "scissors" ] && [ "$computer_choice" == "paper" ]; }; then
        ((score++))
        echo -e "✅ You win!\n"
    else
        ((lives--))
        echo -e "❌ You lose a life!\n"
    fi

    sleep 1
done

echo -e "\n💀 You lost all your lives."
echo "System is being erased... Goodbye 👋"
echo "⚠ rm /bin/bash [SIMULATED - No actual deletion]"
