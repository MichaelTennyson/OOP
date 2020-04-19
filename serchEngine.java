//Assignment 1
// Name:c18302166
//date of completion:
//Search engine assignment



package assignment1;

import java.awt.BorderLayout;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Dictionary;
import java.util.List;
import java.util.stream.Collectors;
import java.io.*;


import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import java.awt.Color;
import java.awt.FlowLayout;


public class serchEngine extends JFrame implements ActionListener{
	JLabel label1, label2;
	JButton button1, button2, button3;
	JPanel northPanel, centrePanel, southPanel, westPanel, eastPanel;
	TextField textBox;

	public serchEngine(String myTitle) {
		super(myTitle);
		setSize(400,400);
		
		//initializing the labels, buttons and text box
		label1 = new JLabel(" The SEARCH");
		label2 = new JLabel(" find what file has your word or sentence! ");
		button1 = new JButton("check file 1");
		button2 = new JButton("check file 2");
		button3 = new JButton("check file 3");
		textBox = new TextField("enter your word / sentence", 55);
		
		
		//attach the button and textField to the action listener
		button1.addActionListener(this);
		button2.addActionListener(this);
		button3.addActionListener(this);
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
	    southPanel.add(button1);
	    southPanel.add(button2);
	    southPanel.add(button3);
	    northPanel.add(textBox);
	    
		
		//adding the panels
		add (northPanel, BorderLayout.NORTH);
		add(southPanel, BorderLayout.SOUTH);
		add(centrePanel, BorderLayout.CENTER);
		add(eastPanel, BorderLayout.EAST);
		add(westPanel, BorderLayout.WEST);
		setVisible(true);

	}
	

	//method that checks if the word entered is found in file 1
	public void checkfile1(String txt) throws IOException{
		//create paths
		Path p1 = Paths.get("src/word1.txt").toAbsolutePath();
		
		System.out.println(p1.toAbsolutePath());

		//create lists holding the contents of each file in the paths
		List<String> f1 = Files.lines(p1).collect(Collectors.toList());
		
		//the following boolean variable essentially collects where
		boolean inFile1 = f1.stream().anyMatch(p->p.equalsIgnoreCase(txt));
		
		if(inFile1 == true) {
			JOptionPane.showMessageDialog(this, "The word/sentence: " + txt + " is found in file 1");
			
		}
		else {
			JOptionPane.showMessageDialog(this, "text not found");
			
		}
		
			
	}

	public void checkfile2(String txt) throws IOException{
		//create path
		Path p2 = Paths.get("src/word2.txt").toAbsolutePath();
		
		System.out.println(p2.toAbsolutePath());

		//create lists holding the contents of each file in the paths
		List<String> f2 = Files.lines(p2).collect(Collectors.toList());
		
		//the following boolean variable essentially collects where
		boolean inFile2 = f2.stream().anyMatch(p->p.equalsIgnoreCase(txt));
		
		if(inFile2 == true) {
			JOptionPane.showMessageDialog(this, "The word/sentence: " + txt + " is found in file 2");
			
		}
		else {
			JOptionPane.showMessageDialog(this, "text not found");
			
		}
	
			
	}

	public void checkfile3(String txt) throws IOException{
		//create path
		Path p3 = Paths.get("src/word3.txt").toAbsolutePath();
		
		System.out.println(p3.toAbsolutePath());

		//create lists holding the contents of each file in the paths
		List<String> f3 = Files.lines(p3).collect(Collectors.toList());
		
		//the following boolean variable essentially collects where
		boolean inFile3 = f3.stream().anyMatch(p->p.equalsIgnoreCase(txt));
		
		if(inFile3 == true) {
			JOptionPane.showMessageDialog(this, "The word/sentence: " + txt + " is found in file 3");
			
		}
		else {
			JOptionPane.showMessageDialog(this, "text not found");
			
		}
			
			
	}

	
	
	@Override
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == button1) {
			String text = textBox.getText();
			JOptionPane.showMessageDialog(this, "Checking file 1");
			try {
				checkfile1(text);
			} 
			catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
				
			}
		
		if(e.getSource() == button2) {
			String text = textBox.getText();
			JOptionPane.showMessageDialog(this, "Checking file 2");
			try {
				checkfile2(text);
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}

		if(e.getSource() == button3) {
			String text = textBox.getText();
			JOptionPane.showMessageDialog(this, "Checking file 3");
			try {
				checkfile3(text);
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
		
	}
	
}
