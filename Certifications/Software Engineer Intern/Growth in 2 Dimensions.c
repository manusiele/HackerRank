'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'countMax' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts STRING_ARRAY upRight as parameter.
 */

function countMax(upRight) {
    // Write your code here
    const coords = upRight.map(s => {
        const [r, c] = s.split(' ').map(Number);
        return [r, c];
    });
    
    let minR = Math.min(...coords.map(([r, c]) => r));
    let minC = Math.min(...coords.map(([r, c]) => c));
    
    return minR * minC;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const upRightCount = parseInt(readLine().trim(), 10);

    let upRight = [];

    for (let i = 0; i < upRightCount; i++) {
        const upRightItem = readLine();
        upRight.push(upRightItem);
    }

    const result = countMax(upRight);

    ws.write(result + '\n');

    ws.end();
}
