# DDU Tutorial

In this section, we give a practical example for writing tests with regard to DDU and its individual terms.
Specifically, we illustrate how to optimize tests for each individual term, i.e. normalized density, diversity, and uniqueness.

## Integer (Single Component Fault)

In this example, we implement an integer with the ability to add, subtract, multiply, and divide.

```java
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
```

In this case, the class has four components (excluding the constructor).
To obtain an optimal normalized density, we could write one test case that covers two methods, such that the matrix looks as follows.

||`add`|`sub`|`mul`|`div`|
|---|---|---|---|---|
|`t1`|1|1|0|0|

However, when we only write one test, the diversity would not be computable and the uniqueness would be `2 / 4 = 0.5`.
The average of average wasted efforts, in this case, is `(0.5 + 0.5 + 2 + 2) / 4 = 1.25`.

To obtain an optimal diversity, we would need to write at least two tests.
For example:

||`add`|`sub`|`mul`|`div`|
|---|---|---|---|---|
|`t1`|1|0|0|0|
|`t2`|0|1|0|0|

This matrix has an optimal diversity of `1.0`, but a normalized density of `0.5` and a uniqueness of `0.75`.
The average of average wasted efforts is `(0 + 0 + 2 + 2) / 4 = 1.0`.

To obtain an optimal uniqueness, it is required to have a unique column for each method.
A straightforward test approach is to write a unit test for each method:

||`add`|`sub`|`mul`|`div`|
|---|---|---|---|---|
|`t1`|1|0|0|0|
|`t2`|0|1|0|0|
|`t3`|0|0|1|0|
|`t4`|0|0|0|1|

For this approach, the normalized density and diversity would be `0.5` and `1.0`, respectively.
Also, this approach is optimal for diagnosing single component faults, i.e. for the faults: `{add}`, `{sub}`, `{mul}`, and `{div}`.
The average of average wasted efforts is `0.0` using Barinel.
However, we could obtain an optimal uniqueness with fewer tests:

||`add`|`sub`|`mul`|`div`|
|---|---|---|---|---|
|`t1`|1|1|0|0|
|`t2`|1|0|1|0|

Although the DDU for this spectra is optimal (normalized density, diversity and uniqueness are `1.0`), the diagnosability is of this test suite is not optimal.
If `div` is faulty, then there is no way to detect the fault because no test is covering `div`; the average of average wasted efforts is `(0 + 0 + 0 + 2) / 4 = 0.5`.


Note that for uniqueness we can compute the minimal number of required tests as follows: `log2(M)`, where `M` is the number of components.

In short, for single component faults, the optimal test approach is to write tests that exercise a single method at a time.
Also, an optimal DDU does not imply optimal diagnosability; we have seen in an example that a test suite with DDU `1.0` is not able to diagnose a single component fault.


## Response (Multiple Component Fault)

```java
class Response {
    String response;

    int v1() {
        if (response == null)
            response = "{ \"key\": 1 }";

        JSONObject json = new JSONObject(response);
        return json.getInt("key");
    }

    int v2() {
        if (response == null)
            response = "{ \"data\": { \"key\": 1 } }";

        JSONObject json = new JSONObject(response);
        return json.getJSONObject("data").getInt("key");
    }
}
```



