package org.stepic.pinch.spark;

import org.apache.spark.Accumulator;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.VoidFunction;
import org.apache.spark.broadcast.Broadcast;

import java.util.Arrays;

public class App {
    public static void main(String[] args) {
        JavaSparkContext sc = new JavaSparkContext("local", "Simple App");
        final Broadcast<Integer> a = sc.broadcast(1);
        final Accumulator<Integer> b = sc.accumulator(1);
        sc.parallelize(Arrays.asList(1, 2, 3)).foreach(new VoidFunction<Integer>() {
            @Override
            public void call(Integer integer) throws Exception {
                b.merge(integer + a.value());
            }
        });
        System.out.println(b);
    }
}