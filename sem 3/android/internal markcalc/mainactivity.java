package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText mark1EditText, mark2EditText, mark3EditText;
    private Button calculateButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mark1EditText = findViewById(R.id.mark1_edittext);
        mark2EditText = findViewById(R.id.mark2_edittext);
        mark3EditText = findViewById(R.id.mark3_edittext);
        calculateButton = findViewById(R.id.calculate_button);

        calculateButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int mark1 = Integer.parseInt(mark1EditText.getText().toString());
                int mark2 = Integer.parseInt(mark2EditText.getText().toString());
                int mark3 = Integer.parseInt(mark3EditText.getText().toString());

                double percentage = calculatePercentage(mark1, mark2, mark3);
                String grade = getGrade(percentage);

                // Send data to second activity
                Intent intent = new Intent(MainActivity.this, ResultActivity.class);
                intent.putExtra("percentage", percentage);
                intent.putExtra("grade", grade);
                startActivity(intent);
            }
        });
    }

    private double calculatePercentage(int mark1, int mark2, int mark3) {
        return (double) (mark1 + mark2 + mark3) / 3.0;
    }

    private String getGrade(double percentage) {
        if (percentage >= 90) {
            return "A";
        } else if (percentage >= 80) {
            return "B";
        } else if (percentage >= 70) {
            return "C";
        } else if (percentage >= 60) {
            return "D";
        } else {
            return "F";
        }
    }
}
