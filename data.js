let products = [
{"name": "Prod1", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod2", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod3", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod4", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod5", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod6", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod7", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod8", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod9", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
{"name": "Prod10", "amount": {"min": 0, "max": 100}, "price": {"min": 0, "max": 100}},
];

let obj_list = [];

class ParentProduct{
    constructor(name) {
        this.name = name;
    }

    show_name() {
        console.log(`Name of this product is ${this.name}`);
    }
}

