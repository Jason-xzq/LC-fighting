package com.company;

import java.util.Stack;

//spent one hour to finish this problem: too slow!
public class DRWOA {
    // you can also use imports, for example:
    // import java.util.*;
    // you can write to stdout for debugging purposes, e.g.
    // System.out.println("this is a debug message");

        private Stack<Integer> sk;
        private final int int_max = (int)Math.pow(2, 20) - 1;
        public boolean operation(String op){
            switch(op){
                case "POP":
                    if(this.sk.empty()){
                        // System.out.println("POP ERROR!\n");
                        return false;
                    }
                    else{
                        this.sk.pop();
                        return true;
                    }
                case "DUP":
                    if(this.sk.empty()){
                        // System.out.println("DUP ERROR!\n");
                        return false;
                    }
                    else{
                        this.sk.push(this.sk.peek());
                        return true;
                    }
                case "+":
                    if(this.sk.size() < 2){
                        // System.out.println("+ ERROR: lack number!\n");
                        return false;
                    }
                    else{
                        int a = this.sk.pop();
                        int b = this.sk.pop();
                        int res = a + b;
                        if(res > this.int_max){
                            // System.out.println("+ ERROR: oveflow!\n");
                            return false;
                        }
                        else{
                            this.sk.push(res);
                            return true;
                        }
                    }
                case "-":
                    if(this.sk.size() < 2){
                        // System.out.println("- ERROR: lack number!\n");
                        return false;
                    }
                    else{
                        int a = this.sk.pop();
                        int b = this.sk.pop();
                        int res = a - b;
                        if(res < 0){
                            // System.out.println("- ERROR: oveflow!\n");
                            return false;
                        }
                        else{
                            this.sk.push(res);
                            return true;
                        }
                    }
                default:
                    int x = Integer.valueOf(op);
                    if(x > this.int_max){
                        // System.out.println("Push Integer ERROR: oveflow!\n");
                        return false;
                    }
                    else{
                        this.sk.push(x);
                        return true;
                    }
            }
        }
        public int solution(String S) {
            // write your code in Java SE 8
            this.sk = new Stack<Integer>();
            String[] buff = S.split(" ");
            for(String op : buff){
                if(!operation(op)){
                    return -1;
                }
            }
            return this.sk.peek();

        }




}
