package com.protonox;

import android.app.Activity;
import android.content.pm.PackageManager;
import android.util.Log;

import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

public class ProtonoxPermissions {
    public static boolean ensurePermissions(Activity activity, String[] permissions, int requestCode) {
        boolean granted = true;
        for (String perm : permissions) {
            int status = ContextCompat.checkSelfPermission(activity, perm);
            if (status != PackageManager.PERMISSION_GRANTED) {
                granted = false;
            }
        }

        if (!granted) {
            ActivityCompat.requestPermissions(activity, permissions, requestCode);
            Log.i("Protonox", "Requested permissions via AndroidX helper");
        }
        return granted;
    }
}
