package nl.tudelft;

class Integer {
    int value;

    Integer(int value) {
        this.value = value;
    }

    Integer add(int value) {
        return new Integer(this.value + value);
    }

    Integer sub(int value) {
        return new Integer(this.value - value);
    }

    Integer mul(int value) {
        return new Integer(this.value * value);
    }

    Integer div(int value) {
        return new Integer(this.value / value);
    }
}
