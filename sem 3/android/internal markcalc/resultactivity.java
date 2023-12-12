package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class ResultActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);

        Intent intent = getIntent();
        double percentage = intent.getDoubleExtra("percentage", 0.0);
        String grade = intent.getStringExtra("grade");

        TextView resultTextView = findViewById(R.id.resu30lt_textview);
        resultTextView.setText("Percentage: " + percentage + "%\nGrade: " + grade);
    }
}
