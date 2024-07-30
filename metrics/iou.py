


def intersection_over_union(boxes_preds:list, boxes_labels:list, box_format="midpoint"):
# def intersection_over_union():
    """
    Calculates intersection over union

    Parameters:
        boxes_preds (list): Predictions of Bounding Boxes (BATCH_SIZE, 4)
        boxes_labels (list): Correct Labels of Boxes (BATCH_SIZE, 4)
        box_format (str): midpoint/corners, if boxes (x,y,w,h) or (x1,y1,x2,y2)

    Returns:
        tensor: Intersection over union for all examples
    """

    if box_format not in ["midpoint","corners"]:
        print("Please use the correct value format arugment : Box format should be either 'midpoint' or 'corners'")

    if box_format == "midpoint":
        pass
        #yet to implement

        # x1_1 = x_center1 - width1 / 2
        # y1_1 = y_center1 - height1 / 2
        # x2_1 = x_center1 + width1 / 2
        # y2_1 = y_center1 + height1 / 2
        
        # x1_2 = x_center2 - width2 / 2
        # y1_2 = y_center2 - height2 / 2
        # x2_2 = x_center2 + width2 / 2
        # y2_2 = y_center2 + height2 / 2

        # max_x1 = max(boxes_preds[0],boxes_labels[0])
        # max_y1 = max(boxes_preds[1],boxes_labels[1])
        # max_x2 = min(boxes_preds[2],boxes_labels[2])
        # max_y2 = min(boxes_preds[3],boxes_labels[3])





    elif box_format == "corners":
        max_x1 = max(boxes_preds[0],boxes_labels[0])
        max_y1 = max(boxes_preds[1],boxes_labels[1])
        max_x2 = min(boxes_preds[2],boxes_labels[2])
        max_y2 = min(boxes_preds[3],boxes_labels[3])

        intersection_area = max(0, max_x2 - max_x1) * max(0, max_y2 - max_y1)
        union_area = ((boxes_labels[2] - boxes_labels[0])*(boxes_labels[1] - boxes_labels[3])) +((boxes_preds[2] - boxes_preds[0])*(boxes_preds[1] - boxes_preds[3])) 


    return max(0,intersection_area / (union_area - intersection_area) )



if __name__ == '__main__':
    box1 = [0.2, 0.2, 0.4, 0.4]  # (x1, y1, x2, y2)
    box2 = [0.3, 0.3, 0.5, 0.5] # (x1, y1, x2, y2)
    print(intersection_over_union(box1, box2,'corners'))
    
