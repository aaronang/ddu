package nl.tudelft;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class ResponseTest {
    Response response;

    @Before
    public void setUp() {
        response = new Response();
    }

    @Test
    public void v1() {
        assertEquals(1, response.v1());
    }

    @Test
    public void v2() {
        assertEquals(1, response.v2());
    }

    @Test
    public void v1v2() {
        response.v1();
        assertEquals(1, response.v2());
    }
}
