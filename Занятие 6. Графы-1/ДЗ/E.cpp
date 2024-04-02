#include <cstdio>

#include <vector>

#include <map>

#include <queue>

#include <string>

#pragma warning(disable : 4996)



using namespace std;



int main() {

    int nMoves;

    scanf("%d", &nMoves);

    map <string, vector<string>> move;  // для реакций

    for (int i = 0; i < nMoves; i++) {

        char bufferFrom[21];

        char bufferTo[21];

        scanf("%20s -> %20s", bufferFrom, bufferTo); // смотрите как читает символы!!!

        string from(bufferFrom);       // перегоняем в строки

        string to(bufferTo);

        move[from].push_back(to);      // реакцию в map

    }

    char bufferFrom[21];

    char bufferTo[21];

    scanf("%20s", bufferFrom);

    string from(bufferFrom);       // перегоняем в строки

    scanf("%20s", bufferTo);

    string to(bufferTo);

    map<string, int> len;

    queue<string> q;

    len[from] = 0;                 // стартовую позицию в map

    q.push(from);                  // и в очередь

    while (!q.empty()) {

        string cur = q.front();    // достаем из очереди очередную хрень

        q.pop();

        if (cur == to) {

            printf("%d", len[cur]);  // мы нашли всю цепочку и печатаем ее длину

            return 0;

        }

        for (string next : move[cur]) {  // по массиву с реакциями для этой хрени

            if (len.count(next) == 0) {   // если в len  такой записи вообще нет

                len[next] = len[cur] + 1; // то нужно ее создать

                q.push(next);

            }

        }

    }

    printf("-1");

    return 0;

}