import 'package:flutter/material.dart';

class Intray extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: 200.0,
        color: Colors.transparent,
        child: Container(
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.only(
                  bottomLeft: const Radius.circular(40.0),
                  bottomRight: const Radius.circular(40.0))),
          child: Text(
            "Intray",
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 2,
              color: Colors.black,
            ),
          ),
        ),
          Center(
            child: Ink(
              decoration: const ShapeDecoration(
                color: Colors.lightBlue,
                shape: CircleBorder(),
              ),
              child: IconButton(
                icon: Icon(Icons.android),
                color: Colors.white,
                onPressed: () {},
              ),
            ),
          ),
        ),
    );
  }
}
