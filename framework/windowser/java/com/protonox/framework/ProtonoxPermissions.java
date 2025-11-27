package com.protonox.framework;

import android.app.Activity;
import android.content.pm.PackageManager;
import android.os.Build;
import android.util.Log;

public class ProtonoxPermissions {
    public static boolean hasPermission(Activity activity, String permission) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
            return true;
        }
        return activity.checkSelfPermission(permission) == PackageManager.PERMISSION_GRANTED;
    }

    public static void requestPermissions(Activity activity, String[] permissions, int requestCode) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
            Log.i("Protonox", "Permissions not required pre-Android 6");
            return;
        }
        activity.requestPermissions(permissions, requestCode);
    }
}
