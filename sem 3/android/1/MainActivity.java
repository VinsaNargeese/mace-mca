package com.example.test1;

//import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {
    EditText user, pwd;
    String u = "vinsa";
    String p ="abc";



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void verify(View v){
        if (v.getId()==R.id.loginButton){
            user = (EditText) findViewById(R.id.username);
            pwd = (EditText) findViewById(R.id.password);
            String a = user.getText().toString();
            String b = pwd.getText().toString();
            if (a.equals(u) && b.equals(p))
                Toast.makeText(this, "sucess", Toast.LENGTH_LONG).show();
            else
                Toast.makeText(this, "invalid", Toast.LENGTH_LONG).show();
        }
    }

}
