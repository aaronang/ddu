package nl.tudelft;

import org.json.JSONObject;

public class Response {
    private String response;

    public int v1() {
        if (response == null) {
            response = "{ \"data\": { \"key\": 1 } }";
        }

        JSONObject json = new JSONObject(response);
        return json.getJSONObject("data").getInt("key");
    }

    public int v2() {
        if (response == null) {
            response = "{ \"key\": 1 }";
        }

        JSONObject json = new JSONObject(response);
        return json.getInt("key");
    }
}
