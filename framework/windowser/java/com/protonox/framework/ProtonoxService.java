package com.protonox.framework;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class ProtonoxService extends Service {
    @Override
    public IBinder onBind(Intent intent) {
        Log.i("Protonox", "Service binding requested: " + intent);
        return null; // placeholder binder
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i("Protonox", "Service started: " + intent);
        return START_STICKY;
    }
}
