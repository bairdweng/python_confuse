//
//  ViewController2.swift
//  confusionExample
//
//  Created by bairdweng on 2020/5/25.
//  Copyright © 2020 bairdweng. All rights reserved.
//

import UIKit

class ViewController2: UIViewController,UITableViewDelegate,UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let hx_myTableViewcell = tableView.dequeueReusableCell(withIdentifier: "DataTableViewCell", for: indexPath) as! DataTableViewCell
        return hx_myTableViewcell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
    }
    
    @IBOutlet weak var hx_TableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()
        hx_TableView.delegate = self
        hx_TableView.dataSource = self
        hx_TableView.register(UINib(nibName: "DataTableViewCell", bundle: nil), forCellReuseIdentifier: "DataTableViewCell")
        // Do any additional setup after loading the view
    }
    
    
}
