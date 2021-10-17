package com.company;
import java.util.*;
import java.util.ArrayList;

public class DRWOA3 {


        private Stack<Integer> sk;
        private int deep = 0;
        private ArrayList<Stack<Integer>> skList;


        public DRWOA3() {
            this.sk = new Stack<Integer>();
            this.skList = new ArrayList<Stack<Integer>>();
            // write your code in Java SE 8
        }

        public void push(int value) {
            this.sk.push(value);
        }

        public int top() {
            if(this.sk.empty()){
                return 0;
            }
            else{
                return this.sk.peek();
            }
        }

        public void pop() {
            if(!this.sk.empty()){
                this.sk.pop();
            }
        }

        public void begin() {
            Stack<Integer> tmp = new Stack<Integer>();
            for (int i = 0; i < this.sk.size(); i++){
                tmp.push(this.sk.get(i));
            }
            this.deep += 1;
            this.skList.add(tmp);
        }

        public boolean rollback() {
            if(this.deep == 0){
                return false;
            }
            this.sk = this.skList.get(this.skList.size()-1);
            this.skList.remove(this.skList.get(this.skList.size()-1));
            this.deep -= 1;
            return true;
        }

        public boolean commit() {
            if(this.deep == 0){
                return false;
            }
            this.skList.remove(this.skList.get(this.skList.size()-1));
            this.deep -= 1;
            return true;
        }

        public static void test() {
            // Define your tests here
            DRWOA3 sol = new DRWOA3();
            sol.push(4);
            sol.begin();                    // start transaction 1
            sol.push(7);                    // stack: [4,7]
            sol.begin();                    // start transaction 2
            sol.push(2);                    // stack: [4,7,2]
            assert sol.rollback() == true;  // rollback transaction 2
            assert sol.top() == 7;          // stack: [4,7]
            sol.begin();                    // start transaction 3
            sol.push(10);                   // stack: [4,7,10]
            assert sol.commit() == true;    // transaction 3 is committed
            assert sol.top() == 10;
            assert sol.rollback() == true;  // rollback transaction 1
            assert sol.top() == 4;          // stack: [4]
            assert sol.commit() == false;   // there is no open
        }

}
