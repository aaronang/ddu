package nl.tudelft;

import org.junit.Test;

import static org.junit.Assert.*;

public class IntegerTest {
    @Test
    public void add() {
        assertEquals(2, new Integer(1).add(2).value);
    }

    @Test
    public void subtract() {
        assertEquals(2, new Integer(4).subtract(2).value);
    }

    @Test
    public void multiply() {
        assertEquals(4, new Integer(2).multiply(2).value);
    }

    @Test
    public void divide() {
        assertEquals(4, new Integer(16).divide(4).value);
    }
}