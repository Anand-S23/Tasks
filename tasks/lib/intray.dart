import 'package:flutter/material.dart';

class Intray extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(children: <Widget>[
        Container(
          padding: EdgeInsets.only(left: 50),
          height: 160,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.only(
                bottomLeft: Radius.circular(40),
                bottomRight: Radius.circular(40)),
            color: Colors.white,
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              Text(
                "Intray",
                style: TextStyle(fontSize: 2,),
              ),
              Container()
            ],
          ),
        ),
        Container(
          height: 60,
          width: 60,
          margin: EdgeInsets.only(
              top: 130, left: MediaQuery.of(context).size.width * 0.5 - 30),
          child: FloatingActionButton(
            child: Icon(
              Icons.add,
              size: 40,
            ),
            backgroundColor: Colors.purple[800],
            onPressed: () {},
          ),
        )
      ]),
      backgroundColor: Colors.grey[600],
    );
  }

  
}
