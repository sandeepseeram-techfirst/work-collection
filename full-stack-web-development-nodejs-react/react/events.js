const EventEmitter = require('events');

const myEmitter = new EventEmitter();

const run =  (numberOfEvents) => {
    setTimeout(() => {
        for(let i = 0; i<numberOfEvents; i++) {
            myEmitter.emit('Before', i+1);
            console.log('Number:' + (i+1));
            myEmitter.emit('After', i+1);
        }
    }, 2000);
}

run(5);

myEmitter.on('Before', (data) => {
    console.log('Process ' + data);
});


myEmitter.on('After', (data) => {
    console.log('Completed ' + data);
});