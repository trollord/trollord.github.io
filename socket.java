import java.io.*;
        import java.net.*;
        public class Myserver {
                public static void main(String[] args){
                    try {
                        ServerSocket ss = new ServerSocket(6666);
                        Socket s = ss.accept();
                        DataInputStream dis = new DataInputStream(s.getInputStream());
                        String str = (String)dis.readUTF();
                        // read the number sent by the client
                        int a = dis.readInt();
                        System.out.println("messageeeee = "+str+a);
                        ss.close();
        
                    }
                    catch(Exception e){
                        System.out.println(e);
                    }
                }    
        }

import java.io.*;
        import java.net.*;
        
        public class Myclient {
            public static void main(String[] args) {
                try {
                    Socket s = new Socket("localhost", 6666);
                    DataOutputStream dout = new DataOutputStream(s.getOutputStream());
                    int a = 10;
                    dout.writeUTF("Hello Serveer");
                    // send a number to the server
                    dout.writeInt(a);
                    dout.flush();
                    dout.close();
                    s.close();
                } catch (Exception e) {
                    System.out.print(e);
                }
            }
        }
