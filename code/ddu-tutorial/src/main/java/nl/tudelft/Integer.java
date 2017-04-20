package nl.tudelft;

class Integer {
    int value;

    Integer(int value) {
        this.value = value;
    }

    Integer add(int value) {
        return new Integer(this.value + value);
    }

    Integer subtract(int value) {
        return new Integer(this.value - value);
    }

    Integer multiply(int value) {
        return new Integer(this.value * value);
    }

    Integer divide(int value) {
        return new Integer(this.value / value);
    }
}
