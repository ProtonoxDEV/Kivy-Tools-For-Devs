package com.protonox;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class ProtonoxService extends Service {
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i("Protonox", "Background service started");
        // TODO: Connect to Python layer via Pyjnius bridge
        return START_STICKY;
    }

    @Override
    public void onDestroy() {
        Log.i("Protonox", "Background service stopped");
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null; // Not a bound service by default
    }
}
