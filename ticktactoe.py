#include <stdio.h>

char board[3][3];
char current_marker;
int current_player;

void initialize_board() {
    char cell = '1';
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = cell++;
}

void print_board() {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf("| ");
        for (int j = 0; j < 3; j++) {
            printf("%c | ", board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int place_marker(int slot) {
    int row = (slot - 1) / 3;
    int col = (slot - 1) % 3;

    if (board[row][col] != 'X' && board[row][col] != 'O') {
        board[row][col] = current_marker;
        return 1;
    }
    return 0;
}

int winner() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return current_player;
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return current_player;
    }

    if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return current_player;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return current_player;

    return 0;
}

void switch_player() {
    current_marker = (current_marker == 'X') ? 'O' : 'X';
    current_player = (current_player == 1) ? 2 : 1;
}

int main() {
    initialize_board();
    current_marker = 'X';
    current_player = 1;

    int slot, won = 0;

    for (int i = 0; i < 9; i++) {
        print_board();
        printf("Player %d (%c), enter your move (1-9): ", current_player, current_marker);
        scanf("%d", &slot);

        if (slot < 1 || slot > 9 || !place_marker(slot)) {
            printf("Invalid move! Try again.\n");
            i--;
            continue;
        }

        won = winner();
        if (won != 0) {
            print_board();
            printf("Player %d wins!\n", current_player);
            return 0;
        }

        switch_player();
    }

    print_board();
    printf("It's a draw!\n");
    return 0;
}
