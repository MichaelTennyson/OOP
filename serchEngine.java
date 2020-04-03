//Assignment 1
// Name:c18302166
//date of completion:
//Search engine assignment



package assignment1;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class serchEngine extends JFrame implements ActionListener{
	JLabel label1, label2;
	JButton button1, button2;
	JPanel northPanel, centrePanel, southPanel, westPanel, eastPanel;
	TextField textBox;
	JFileChooser f1, f2, f3;
	File word1 = new File("D:\\Eclipse\\OOPsem2\\src\\word1.txt");
	File word2 = new File("D:\\Eclipse\\OOPsem2\\src\\word2.txt");
	File word3 = new File("D:\\Eclipse\\OOPsem2\\src\\word3.txt");

	public serchEngine(String myTitle) {
		super(myTitle);
		setSize(300,300);
		
		//initialising the labels, buttons and text box
		label1 = new JLabel(" The search engine ");
		label2 = new JLabel(" find what file has your word ");
		button1 = new JButton("Open files");
		button2 = new JButton("Enter");
		textBox = new TextField("enter your word / sentence", 20);
		f1 = new JFileChooser( word1);
		f2 = new JFileChooser(word2);
		f3 = new JFileChooser( word3);
		
		
		//attach the buttons to the action listener
		button1.addActionListener(this);
		textBox.addActionListener(this);
		
		// setting up my border layout
		BorderLayout bL1 = new BorderLayout();
		setLayout(bL1);
		
		//set up panels
		northPanel = new JPanel();
		centrePanel = new JPanel();
		southPanel = new JPanel();
		westPanel = new JPanel();
		eastPanel = new JPanel();
		
		//positioning panels
		westPanel.add(label1);
	    eastPanel.add(label2);
	    centrePanel.add(button1);
	    southPanel.add(textBox);
	    
		
		//adding the panels
		add (northPanel, BorderLayout.NORTH);
		add(southPanel, BorderLayout.SOUTH);
		add(centrePanel, BorderLayout.CENTER);
		add(eastPanel, BorderLayout.EAST);
		add(westPanel, BorderLayout.WEST);
		setVisible(true);

	}


	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == button1) {
			//files are opened
			File file1 = f1.getSelectedFile();
			File file2 = f2.getSelectedFile();
			File file3 = f3.getSelectedFile();
			JOptionPane.showMessageDialog(this, "files opened");
		}
		if(e.getSource() == button2) {
			String text = textBox.getText();
			JOptionPane.showMessageDialog(this, "Checking now");
			if(text ==  f1.open()){
				
				
			}
		}
		
		
	}

}
