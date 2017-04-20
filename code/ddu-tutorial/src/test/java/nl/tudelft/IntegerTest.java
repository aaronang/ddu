package nl.tudelft;

import org.junit.Test;

import static org.junit.Assert.*;

public class IntegerTest {
    @Test
    public void add() {
        assertEquals(3, new Integer(1).add(2).value);
    }

    @Test
    public void sub() {
        assertEquals(2, new Integer(4).sub(2).value);
    }

    @Test
    public void mul() {
        assertEquals(4, new Integer(2).mul(2).value);
    }

    @Test
    public void div() {
        assertEquals(4, new Integer(16).div(4).value);
    }

    @Test
    public void addSub() {
        assertEquals(2, new Integer(1).add(4).sub(3).value);
    }

    @Test
    public void addMul() {
        assertEquals(2, new Integer(1).add(1).mul(1).value);
    }
}