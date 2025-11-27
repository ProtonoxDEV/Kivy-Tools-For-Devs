package com.protonox.framework;

import android.content.Context;
import android.os.Build;
import android.os.Environment;
import android.util.Log;

import java.io.File;

public class ProtonoxStorage {
    public static File getAppExternalDir(Context context) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            return context.getExternalFilesDir(null);
        }
        return Environment.getExternalStorageDirectory();
    }

    public static void logStoragePaths(Context context) {
        File base = getAppExternalDir(context);
        Log.i("Protonox", "External directory: " + base);
    }
}
