package com.protonox;

import android.content.Context;
import android.net.Uri;
import android.util.Log;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class ProtonoxStorage {
    public static boolean saveBytes(Context context, String relativePath, byte[] data) {
        try {
            File target = new File(context.getFilesDir(), relativePath);
            target.getParentFile().mkdirs();
            OutputStream os = new FileOutputStream(target);
            os.write(data);
            os.close();
            Log.i("Protonox", "Saved " + data.length + " bytes to " + target.getAbsolutePath());
            return true;
        } catch (Exception e) {
            Log.e("Protonox", "Failed to save bytes", e);
            return false;
        }
    }

    public static byte[] readBytes(Context context, String relativePath) {
        try {
            File target = new File(context.getFilesDir(), relativePath);
            InputStream is = new FileInputStream(target);
            byte[] buffer = new byte[(int) target.length()];
            int read = is.read(buffer);
            is.close();
            if (read != buffer.length) {
                Log.w("Protonox", "Read partial data from " + relativePath);
            }
            return buffer;
        } catch (Exception e) {
            Log.e("Protonox", "Failed to read bytes", e);
            return null;
        }
    }

    public static boolean saveContentUri(Context context, Uri uri, String relativePath) {
        try {
            InputStream is = context.getContentResolver().openInputStream(uri);
            File target = new File(context.getFilesDir(), relativePath);
            target.getParentFile().mkdirs();
            OutputStream os = new FileOutputStream(target);
            byte[] buffer = new byte[8192];
            int read;
            while ((read = is.read(buffer)) != -1) {
                os.write(buffer, 0, read);
            }
            os.close();
            is.close();
            return true;
        } catch (Exception e) {
            Log.e("Protonox", "Failed to save URI", e);
            return false;
        }
    }
}
