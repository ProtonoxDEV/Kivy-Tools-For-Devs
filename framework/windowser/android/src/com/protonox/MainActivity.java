package com.protonox;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.i("Protonox", "MainActivity bootstrapped - wire this into python-for-android bootstrap");
    }
}
